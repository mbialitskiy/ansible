from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

import github


from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):
        ret = []
        creds = [terms[0],terms[1]]
        try:
            git = github.Github(creds[0], creds[1])
        except:
            raise github.GithubException
        else:
            if len(terms) == 2:
                Display().debug("Provided 2 params. Get all repos for user")
                repos = git.get_user().get_repos()
                for rep in repos:
                    ret.append(rep.name)
            if len(terms) == 3:
                Display().debug("Provided 3 params. Getting all files in repo {0}".format(terms[2]))
                repo = git.get_user().get_repo(terms[2])
                for item in repo.get_contents('/'):
                    ret.append(item.path)
            if len(terms) == 4:
                Display().debug("Provided 4 params. Checking if file exists in repo {0}".format(terms[2]))
                repo = git.get_user().get_repo(terms[2])
                for item in repo.get_contents('/'):
                    if item.name == terms[3]:
                        ret.append('File {0} exists. Last modified date: {1}'.format(terms[3],item.last_modified))
                        break
                if len(ret) == 0:
                    ret.append('File not found')
        return ret
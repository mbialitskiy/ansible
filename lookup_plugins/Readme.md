You need PyGithub to run this plugin
usage:

- debug:
      msg : "{{ lookup('lookup_git', username, password) }} " - show all repos for user

- debug:
      msg : "{{ lookup('lookup_git', username, password, repository_name) }} " - show files in repo

- debug:
      msg : "{{ lookup('lookup_git', username, password, repository_name, file) }} " - find file in repo

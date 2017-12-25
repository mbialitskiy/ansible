from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

        result['_ansible_verbose_always'] = True


        link_file = self._task.args.get('file', None)

        with open(link_file, "r") as file:
            link = file.read().replace('\n', '')

        pass_vars = dict()
        pass_vars.update(
            ansible_version=task_vars['ansible_version'],
            url = link
        )

        new_module_args = dict()
        new_module_args.update(
            dict(
                url=link
            ),
        )

        result.update(
            self._execute_module(
                module_name='wtar',
                module_args=new_module_args,
            )
        )

        return result
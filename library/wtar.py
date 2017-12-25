from ansible.module_utils.basic import AnsibleModule
import urllib, tarfile

def main():


    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str')
        )
    )

    args = module.params

    msg = []

    if (args['url'].endswith("tar.gz")):
        urllib.urlretrieve(args['url'],args['url'].split('/')[-1])
        tar = tarfile.open(args['url'].split('/')[-1])
        tar.extractall()
        tar.close()
        msg.append('Downloaded and extracted to current dir')
    else:
        msg.append('Not a tar.gz file')

    module.exit_json(module_msg=msg)

if __name__ == '__main__':
    main()

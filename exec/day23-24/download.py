from ansible.module_utils.basic import AnsibleModule
from wget import download

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url = dict(required=True,type='str'),
            dest = dict(required=True,type='str')
        )
    )
    download(module.params['url'],module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
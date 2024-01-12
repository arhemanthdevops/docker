import json
import pandas as pd

# JSON data as a string (replace this with your actual JSON string)
json_data = '''
[
    {
        "Id": "sha256:043dab2e3ae8333462b2ac2292541bf24d4e37547f6aad2ddce1aca35e47fc9a",
        // ...[
    {
        "Id": "sha256:043dab2e3ae8333462b2ac2292541bf24d4e37547f6aad2ddce1aca35e47fc9a",
        "RepoTags": [
            "python:latest"
        ],
        "RepoDigests": [],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2024-01-08T11:23:21.074854494Z",
        "Container": "",
        "ContainerConfig": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": null,
            "Cmd": null,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "DockerVersion": "",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
                "PYTHON_VERSION=3.9.18",
                "PYTHON_PIP_VERSION=23.0.1",
                "PYTHON_SETUPTOOLS_VERSION=58.1.0",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py",
                "PYTHON_GET_PIP_SHA256=9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6"
            ],
            "Cmd": [
                "python",
                "./user-input.py"
            ],
            "ArgsEscaped": true,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "/usr/src/app",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 126391824,
        "VirtualSize": 126391824,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/osowr9wfyf3tdjthdmccdznrs/diff:/var/lib/docker/overlay2/c0ff77dbe39438175053300432bfb0f14642ea1a990c5e32900b4d9f803a8a72/diff:/var/lib/docker/overlay2/8af31a2a3d66fe3de787a10252a73fafb05e8cca1bdb5d97f0de91c15c0d17fd/diff:/var/lib/docker/overlay2/161b3bf0e540f94f548ef08afa4a9137087ea2e3c7fa5e8b5a7b18c46f9f09b3/diff:/var/lib/docker/overlay2/9ff9c56865a10eba222569cdd824c5f40934a3717525acfaa88a1fe9bc559e5a/diff:/var/lib/docker/overlay2/48238e2df4da6e9b9516a7baaa52c69bfaa1956c90aa342a2e0dea8f936ced73/diff",
                "MergedDir": "/var/lib/docker/overlay2/73n3gp6w2wthyhkat834u5l04/merged",
                "UpperDir": "/var/lib/docker/overlay2/73n3gp6w2wthyhkat834u5l04/diff",
                "WorkDir": "/var/lib/docker/overlay2/73n3gp6w2wthyhkat834u5l04/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:7292cf786aa89399bca4e3edd105d3b2ee0683a46ef1f5ff436c0f9d1d49e765",
                "sha256:384858ccd7ef0b8449b819cd61b39fc4560e476326c0bd5168523907c26bf527",
                "sha256:661ecc6e457f9c02b88f17feb970479d46de0f5718bb6150a9fe82a647ace545",
                "sha256:a1e3c54d75a8292d27947a0da787b866c9f5321b7ed6c9d4846dda49e9db929d",
                "sha256:4cec408baceeb81dbf260406a6f6fbb83b8f333565be1bfc27fdc057a611d691",
                "sha256:6b742e3cf930b78b0fc220cce41dc5e861ecb4bf1c1b112be8631b28b1ed7405",
                "sha256:580d53c25cbdaf206575d068a08bf2edae2ff9dd058871ad6cceb6a6720433b5"
            ]
        },
        "Metadata": {
            "LastTagTime": "2024-01-08T11:23:21.119725626Z"
        }
    }
] 
    }
]
'''

# Convert JSON string to Python list
data = json.loads(json_data)

# Convert to DataFrame
df = pd.json_normalize(data)

# Print the DataFrame
print(df)


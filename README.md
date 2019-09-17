# python-terraform-directory-tree-generator
Generates a directory structure and will also generate empty terraform files.

## How to use
```
ROOT_DIRECTORY='.'
cat <<EOF > tree.txt
terraform/
terraform/main.tf
scripts/
scripts/helpers/
scripts/base/
EOF
python struct.py ${ROOT_DIRECTORY} tree.txt
ls *
```

## Requirements
The following are a list of requirements:
1. python 2.7 or above.


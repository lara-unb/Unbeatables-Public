#!/usr/bin/env bash
### interrompo o script caso algum passo retorno != 0
set -e

if [[ -n $DEBUG ]]; then
    verbose="-v"
fi

mv $verbose $INIT_DIR/exec-suid /usr/bin/
chmod $verbose u+s /usr/bin/exec-suid

for var in "$@"
do
    echo "Corrigindo permissões para: $var"
    find "$var"/ -name '*.sh' -exec chmod $verbose a+x {} +
    find "$var"/ -name '*.desktop' -exec chmod $verbose a+x {} +
    chgrp -R 0 "$var" && chmod -R $verbose a+rw "$var" && find "$var" -type d -exec chmod $verbose a+x {} +
done



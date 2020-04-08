#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR || exit 1
#apollo-codegen generate ./graphql/query/*.graphql --target typescript --output ./graphql/query.ts && apollo-codegen generate ./graphql/mutation/*.graphql --target typescript --output ./graphql/mutation.ts
apollo-codegen generate **/*.tsx --target typescript --output ./graphql/operations.ts
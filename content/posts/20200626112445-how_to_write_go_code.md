+++
title = "How To Write Go Code"
author = ["John Doe"]
draft = false
+++

last modified
: 2020-06-26 18:24:11


tags
: [Go]({{< relref "20200615074513-go" >}})

source
: [How To Write Go Code](x-devonthink-item://D08DF1DC-28F0-4E3C-B30B-2AAB6DFB3685)


## Code Organization {#code-organization}


### Module {#module}

-   collection of packages
-   usually one directory contains one module
-   module has `go.mod` file containing description of the it


### Package {#package}

-   collection of source code files
-   source code files in one package share the same scope
    functions, variables, constants


## Init, run, test, install {#init-run-test-install}


### Init {#init}

`go mod init <module prefix>`
declare a module and create a `go.mod` automatically


### Run {#run}

`go run <main package file>`


### Test {#test}

`go test`

-   file name convention: `xxx_test.go`
-   test function name convention: `func TestXXX(t *testing.T)`


### Install {#install}

`go install <path>`

-   if currently in module root dir, `<path>` can be omitted
-   module will be installed to:
    -   if `GOBIN` is set, binary goes to that directory
    -   if `GOPATH` is set, binary goes to the first directory's `bin` subdir

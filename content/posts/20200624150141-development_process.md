+++
title = "Development Process"
author = ["John Doe"]
draft = false
+++

{{< figure src="/ox-hugo/2020-06-24_17-02-51_CleanShot 2020-06-24 at 17.01.16@2x.png" >}}


## Create a [Service]({{< relref "20200624164129-service" >}}) with [BONES]({{< relref "20200624155901-bones" >}}) {#create-a-service--20200624164129-service-dot-md--with-bones--20200624155901-bones-dot-md}

`bones --new`


## Enable [Pipeline]({{< relref "20200624160531-pipeline" >}}) {#enable-pipeline--20200624160531-pipeline-dot-md}

1.  go to pipelines.amazon.com, click \`Resume [Promotion]({{< relref "20200624160603-promotion" >}})\`
2.  enable automatic promotions for all [Stage]({{< relref "20200624160706-stage" >}})
    click arrows between stages to edit promotions: click \`Turn on all\`


## Create [Workspace]({{< relref "20200624160957-workspace" >}}) with [Brazil]({{< relref "20200624161102-brazil" >}}) {#create-workspace--20200624160957-workspace-dot-md--with-brazil--20200624161102-brazil-dot-md}

`brazil workspace create --root BT101`

1.  show details of the workspace
    `brazil ws show`
2.  use [VersionSet]({{< relref "20200624161325-versionset" >}}) created by BONES
    `brazil ws use --versionset <versionset name>`
3.  run platform override to ensure all package compile
    `brazil ws --use --platform <name>`
4.  add [Package]({{< relref "20200624161524-package" >}}) to workspace
    `brazil ws use --package <package name>`


## Build Changes {#build-changes}

1.  go to package root dir
2.  before building, make sure the version set is the latest
    `brazil ws --sync --metadata`
3.  build
    build: `brazil-build`
    test: `brazil-build test`
    build, run unit tests, check styles: `brazil-build release`


## Commit changes {#commit-changes}


## Create CR {#create-cr}

1.  go to package root dir
2.  `cr`
3.  after approved, merge and wait for pipeline to finish


## Clean up services {#clean-up-services}

1.  Delete the pipeline
2.  Deprecate packages
3.  Deprecate versionset
4.  Delete [Workspace]({{< relref "20200624160957-workspace" >}})
    `brazil ws delete --root workplace/<name>`
    `brazil ws delete --root bonts/<name>`

properties([pipelineTriggers([pollSCM('* * * * * ')])])
node {
    stage("clone") {
        git branch: 'master', url: 'https://github.com/sharonazrd/DevOps2412.git'
    }
    stage("show files"){
        sh "ls -l"
    }
}

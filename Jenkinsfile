properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("one"){
        git "https://github.com/asafida/devops2402.git"
    } 
    stage("bla") {
    sh "ls -l"
    }
}

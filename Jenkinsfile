properties([parameters([string(defaultValue: 'asaf', description: 'what is your name?', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("one"){
        git "https://github.com/asafida/devops2402.git"
    } 
    stage("bla") {
    sh "ls -l"
    }
}


parser grammar CsExtraGitlab;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_gitlab:
    AN_GITLAB
    BRACE_OPEN
    NL*
    an_gitlab_branch_declaration+
    NL*
    BRACE_CLOSE
    ;

an_gitlab_branch_declaration:

    an_gitlab_branch_name
    EQUALS GT

    an_gitlab_deployment_name
    BRACE_OPEN
    NL*
    an_gitlab_deployment_host
    (COMA? an_gitlab_deployment_variable)*
    NL*
    BRACE_CLOSE
    NL*
    ;

an_gitlab_branch_name:
    id_or_kw
    ;

an_gitlab_deployment_name:
    id_or_kw
    ;

an_gitlab_deployment_host:
    classname
    ;

an_gitlab_deployment_variable:
    NL*
    an_gitlab_deployment_variable_name
    EQUALS
    an_gitlab_deployment_variable_value
    ;

an_gitlab_deployment_variable_name:
    id_or_kw
    ;

an_gitlab_deployment_variable_value:
    STRING_DQ | STRING_SQ | DIGIT | id_or_kw
    ;



parser grammar AppExtensionGitlab;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_gitlab:
    AN_GITLAB
    BRACE_OPEN
    NL*
    an_gitlab_test_declaration?
    NL*
    an_gitlab_branch_declaration+
    NL*
    BRACE_CLOSE
    ;

an_gitlab_test_declaration:
    an_gitlab_test_declaration_selenium_pytest
    ;

an_gitlab_test_declaration_selenium_pytest:
    KW_SELENIUM_PYTEST
    BRACE_OPEN
    NL*
    an_gitlab_test_services?
    NL*
    (an_gitlab_deployment_variable COMA?)*
    NL*
    BRACE_CLOSE
    ;

an_gitlab_test_services:
    KW_SERVICES
    BRACE_OPEN
    NL*
    (an_gitlab_test_service (COMA an_gitlab_test_service)*)?
    NL*
    BRACE_CLOSE
    ;

an_gitlab_test_service:
    NL*
    an_gitlab_test_service_name
    (BRACE_OPEN
    NL*
    (an_gitlab_deployment_variable COMA?)*
    NL*
    BRACE_CLOSE)?
    ;

an_gitlab_test_service_name:
    id_or_kw
    ;


an_gitlab_branch_declaration:

    an_gitlab_branch_name
    NL*
    an_gitlab_branch_deploy_type
    NL*
    an_gitlab_deployment_name
    BRACE_OPEN
    NL*
    an_gitlab_deployment_host
    (COLON NL* (an_gitlab_deployment_variable COMA?)*)?
    NL*
    BRACE_CLOSE
    NL*
    ;

an_gitlab_branch_deploy_type:
    (EQUALS|APPROX) GT
    ;

an_gitlab_branch_name:
     (id_or_kw
    |DASH
    |STAR
    |SLASH)+
    ;

an_gitlab_deployment_name:
    (id_or_kw
    |DASH
    |SLASH
    |STAR)+
    ;

an_gitlab_deployment_host:
    (id_or_kw
    |DASH
    |STAR
    |DOT)+
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


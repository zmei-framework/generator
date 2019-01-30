import React from 'react';
import {Suspense, lazy} from "react";
import {BrowserRouter, StaticRouter} from "react-router-dom";
import Switch from "react-router-dom/es/Switch";
import Route from "react-router-dom/es/Route";

{% if pages|length > 15 %}
{% for app_name, page_name, uri in pages %}
const {{ app_name }}{{ page_name }} = lazy(() => import("./{{ app_name|lower }}/pages/{{ page_name }}"));{% endfor %}
{%- else -%}
{% for app_name, page_name, uri in pages %}
import {{ app_name }}{{ page_name }} from "./{{ app_name|lower }}/pages/{{ page_name }}";{% endfor %}
{% endif %}

class {{ name }}Router extends React.Component {
    render() {

        return (
            <BrowserRouter basename="/">
                <Switch>
                   {% for app_name, page_name, uri in pages -%}
                   <Route path="{{ uri }}" exact
                          render={matchprops => (
                          <Suspense fallback={<></>}>
                            <{{ app_name }}{{ page_name }} {...matchprops} />
                         </Suspense>
                      )}
                   />
                   {% endfor %}
                </Switch>
            </BrowserRouter>
        );
    }
}

export default {{ name }}Router;

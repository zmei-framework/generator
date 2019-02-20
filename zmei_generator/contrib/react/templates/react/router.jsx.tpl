import React from 'react';
import {Suspense, lazy} from "react";
import {BrowserRouter, StaticRouter} from "react-router-dom";
import Switch from "react-router-dom/es/Switch";
import Route from "react-router-dom/es/Route";
import { include } from "named-urls";

{% if pages|length > 50 %}
{% for app_name, page_name, uri in pages %}
const {{ app_name }}{{ page_name }} = lazy(() => import("./{{ app_name|lower }}/ui/{{ page_name }}"));{% endfor %}
{%- else -%}
{% for app_name, page_name, uri in pages %}
import {{ app_name }}{{ page_name }} from "./{{ app_name|lower }}/ui/{{ page_name }}";{% endfor %}
{% endif %}

export const routes = {
{% for app_name, pages in pages_index.items() %}
    {{ app_name }}: include('', { {% for page_name, page_uri in pages.items() %}
        {{ page_name }}: '{{ page_uri }}',
    {% endfor %}
    }),
{% endfor %}
}

class {{ name }}Router extends React.Component {
    render() {

        return (
            <BrowserRouter basename="/">
                <Switch>
                   {% for app_name, pages in pages_index.items() %}{% for page_name, uri in pages.items() -%}
                   <Route path={ routes.{{ app_name }}.{{ page_name }} } exact
                          render={matchprops => (
                          <Suspense fallback={<></>}>
                            <{{ to_camel_case(app_name) }}{{ to_camel_case(page_name) }}Ui {...matchprops} />
                         </Suspense>
                      )}
                   />
                   {% endfor %}{% endfor %}
                </Switch>
            </BrowserRouter>
        );
    }
}

export default {{ name }}Router;

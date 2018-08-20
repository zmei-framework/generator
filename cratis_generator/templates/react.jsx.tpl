{{ imports }}

export class {{ name }} extends React.Component {
    render() {
        {{ body|indent(8) }}
        return (
            {{ source|indent(12) }}
        );
    }
}

import {Form, Field, Formik} from "formik";
import React from 'react';
import {FormGroup, Label, Alert} from "reactstrap";
import Select from "react-select";

export class SchemaForm extends React.Component {

    inputField = (params) => (field) => {
        var extraProps = {};

        if (field.placeholder != null) extraProps['placeholder'] = field.placeholder;
        // if (params.handleChange != null) extraProps['onChange'] = params.handleChange;
        return (<Field name={field.name} type={field.type} id={field.name}
                       onChange={params.handleChange}
                       onBlur={params.handleBlur}
                       className={`form-control ${((field.serverErrors) || (params.errors[field.name] && params.touched[field.name])) && 'is-invalid'}`}
                       value={params.values[field.name]} {...extraProps} />);
    };
    checkbox = (params) => (field) => (
        <div className="form-check">
            <label className="form-check-label">
                <input name={field.name} className="form-check-input" onChange={this.props.handleChange} type="checkbox"
                       checked={params.values[field.name]}/> {field.description}
            </label>
        </div>
    );

    textarea = (params) => (field) => (
        <textarea name={field.name} className="form-control" onChange={this.props.handleChange} id={field.name}
                  value={params.values[field.name]} rows={field.rows || 3}/>);

    radio = (params) => (field) =>
        field.options.map((option) => (
            <div className="form-check" key={option.value}>
                <label className="form-check-label">
                    <input name={field.name} className="form-check-input" onChange={params.handleChange}
                           type="radio"
                           id={field.name + '_' + option.value} value={option.value}
                           checked={params.values[field.name] === option.value}/> {option.title}
                </label>
            </div>
        ));

    select = (params) => (field) => {
        return <Select
            // classNamePrefix="select"
            value={field.options ? field.options.find(option => option.value === params.values[field.name]) : ''}
            onChange={(option) => params.setFieldValue(field.name, option.value)}
            className={`select-basic-single ${((field.serverErrors) || (params.errors[field.name] && params.touched[field.name])) && 'is-invalid'}`}
            name={field.name}
            options={field.options}
         />};

    renderField = (params) => (field) => {
        const fieldType = {
            text: this.inputField,
            choices: this.select,
            checkbox: this.checkbox,
            email: this.inputField,
            password: this.inputField,
            url: this.inputField,
            number: this.inputField,
        }[field.type](params);

        return <FormGroup key={field.name}>
                <Label for={field.name}>{field.title}</Label>
                {fieldType(field)}
                {params.errors[field.name] && params.touched[field.name] ? <div className="invalid-feedback">{params.errors[field.name]}</div> : null}
                {field.serverErrors? field.serverErrors.map((error) => <div key={error} className="invalid-feedback">{error}</div>) : null}
                {field.helpText && (<small className="form-text text-muted">{field.helpText}</small>)}
            </FormGroup>
    };

    buildValidationSchema() {

    }

    renderForm = (params) => {
        return this.props.form.schema.fields.map(this.renderField(params))
    };

    render() {
        if (!this.props.form) return <></>;

        return (
            <Formik
                validationSchema={this.buildValidationSchema()}
                initialValues={this.props.form.initial}

                {...this.props}
            >
                {(params) => (
                    <Form>
                        <div className="form-body">
                            {this.props.form.errors.map((error) => <Alert key={error} color="warning">{error}</Alert>)}
                            {this.renderForm(params)}
                        </div>

                        {this.props.children}
                    </Form>
                )}
            </Formik>
        );
    }
}

export default SchemaForm;
import React from "react";
import { Formik, Field, Form, ErrorMessage } from 'formik';
import {loginService} from "../services/loginService"

export default class Login extends React.Component {
    constructor(props) {
        super(props);

        // redirect to home if already logged in
        if (loginService.currentUserValue) { 
            this.props.history.push('/');
        }
    }

    render () {
        return(
            <div className="login">
                <Formik
                    initialValues={{
                        username: '',
                    }}
                    onSubmit={({ username}, { setStatus, setSubmitting }) => {
                        setStatus();
                        loginService.login(username)
                            .then(
                                user => {
                                    const { from } = this.props.location.state || { from: { pathname: "/" } };
                                    this.props.history.push(from);
                                },
                                error => {
                                    setSubmitting(false);
                                    setStatus(error);
                                }
                            );
                    }}
                    render={({ errors, touched, isSubmitting }) => (
                        <Form>
                            <div className="form-group">
                                <label htmlFor="username">Username</label>
                                <Field name="username" type="text" className={'form-control' + (errors.username && touched.username ? ' is-invalid' : '')} />
                                <ErrorMessage name="username" component="div" className="invalid-feedback" />
                            </div>
                            <div className="form-group">
                                <button type="submit" className="btn btn-primary" disabled={isSubmitting}>Login</button>
                            </div>
                        </Form>
                    )}
                ></Formik>
            </div>
            
        )
    }
}
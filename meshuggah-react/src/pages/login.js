import React from "react";
import { Formik, Field, Form, ErrorMessage } from 'formik';
import {loginService} from "../services/loginService"
import { redirect, useNavigate } from "react-router";
// import {useNavigate} from 'react-router-dom

export default class Login extends React.Component {

    constructor(props) {
        super(props);

    }

    render () {
        // const navigate = useNavigate();
        return(
            <div className="login">
                <Formik
                    initialValues={{
                        username: '',
                    }}
                    onSubmit={({ username}, { setStatus }) => {
                        setStatus();
                        loginService.login(username)
                            .then(
                                this.props.navigate('/')
                            );
                    }}
                    render={({ errors, touched, isSubmitting }) => (
                        <Form>
                            <h1> Login</h1>
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
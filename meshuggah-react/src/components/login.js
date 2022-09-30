import React from "react";

export default class Login extends React.Component {
    render () {
        return(
            <div className="login">
                <h1>Login</h1>
                <label htmlFor="usenameInput"> Username: </label>
                <input id="usernameInput" name="usernameInput" type="text"></input>
                <button>Login</button>
            </div>
        )
    }
}
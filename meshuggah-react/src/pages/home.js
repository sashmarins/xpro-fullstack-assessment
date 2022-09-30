import React from 'react';

import { loginService } from '../services/loginService';
import { userService } from '../services/userService';

export default class Home extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            currentUser: loginService.currentUserValue,
            userFromApi: null
        };
    }

    componentDidMount() {
        const { currentUser } = this.state;
        userService.getById(currentUser.id).then(userFromApi => this.setState({ userFromApi }));
    }

    render() {
        const { currentUser, userFromApi } = this.state;
        return (
            <div className='home'>
                <h1>Home</h1>
                <p>You're logged in with React</p>
                <p>Your role is: <strong>{currentUser.role}</strong>.</p>
                <p>This page can be accessed by all authenticated users.</p>
                <div>
                    Current user from secure api end point:
                    {userFromApi &&
                        <ul>
                            <li>{userFromApi.first_name} {userFromApi.last_name}</li>
                        </ul>
                    }
                </div>
            </div>
        );
    }
}
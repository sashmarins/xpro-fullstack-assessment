import React from "react";
import CompanyDropdown from "./companyDropdown";
import {Link} from 'react-router-dom'
import { loginService } from '../services/loginService';
import history from '../services/history'

export default class Sidebar extends React.Component {

    logout() {
        loginService.logout();
        history.go('/login');
    }

    render () {
        return(
            <div className="Sidebar">
                <h1> Meshuggah </h1>
                <div className="navitems">
                    <Link to="/" className="homelink">Home</Link>
                    <div>
                        <a onClick={this.logout} className="nav-item nav-link">Logout</a>
                    </div>
                </div>
                <CompanyDropdown/>
            </div>
        )
    }
}
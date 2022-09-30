import './App.css';
import Login from './pages/login';
import Home from './pages/home';
import Sidebar from './components/sidebar';
import UserList from './components/userList';
import history from './services/history'
import role from './services/role'
import { loginService } from './services/loginService';
import React from 'react';
import { Route, Link, Routes } from 'react-router-dom';
import { BrowserRouter as Router} from 'react-router-dom';

export default class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        currentUser: null,
        isAdmin: false,
        isClient: false
    };
}

componentDidMount() {
    loginService.currentUser.subscribe(x => this.setState({
        currentUser: x,
        isAdmin: x && x.role === role.Admin,
        isClient: x && x.role === role.Client
    }));
}

  logout() {
      loginService.logout();
      history.push('/login');
  }

  render() {
    const { currentUser } = this.state;
    return (
        <Router history={history}>
            <div>
                {currentUser &&
                    <nav className="navbar navbar-expand navbar-dark bg-dark">
                        <div className="navbar-nav">
                          <Sidebar/>
                        </div>
                    </nav>
                }
                <div className="jumbotron">
                    <div className="container">
                        <div className="row">
                            <div className="col-md-6 offset-md-3">
                              <Routes>
                                <Route exact path="/" element={<Home/>} />
                                <Route path="/login" element={<Login/>} />
                              </Routes>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </Router>
    );
}
}

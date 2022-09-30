import { BehaviorSubject } from 'rxjs';

const currentUserSubject = new BehaviorSubject(JSON.parse(localStorage.getItem('currentUser')));

const apiUrl = "http://127.0.0.1:8000/api";

export const loginService = {
    login,
    logout,
    currentUser: currentUserSubject.asObservable(),
    get currentUserValue () { return currentUserSubject.value }
};

function login(username) {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({username: username})
    };

    return fetch(`${apiUrl}/users/login/`, requestOptions)
        .then(user => user.json())
        .then(jsondata => {
            localStorage.setItem('currentUser', jsondata);
            currentUserSubject.next(jsondata);
        })
        .catch(error => {
            alert("your login is invalid")
            return error;
        });
}

function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('currentUser');
    currentUserSubject.next(null);
}

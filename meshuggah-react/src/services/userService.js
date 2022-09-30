const apiUrl = "http://127.0.0.1:8000/api";

export const userService = {
    getAll,
    getById
};

function getAll() {
    const requestOptions = { method: 'GET'};
    return fetch(`${apiUrl}/users`, requestOptions);
}

function getById(id) {
    const requestOptions = { method: 'GET'};
    return fetch(`${apiUrl}/users/${id}`, requestOptions);
}
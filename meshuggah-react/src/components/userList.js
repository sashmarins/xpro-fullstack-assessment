import React from "react";

export default class UserList extends React.Component {
// https://www.geeksforgeeks.org/how-to-create-a-table-in-reactjs/

    render () {
        return(
            <div className="UserList">
                <table>
                    <tr>
                        <th>Last Name</th>
                        <th>First Name</th>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Role</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Address</th>
                        <th>Client ID</th>
                    </tr>
                    <tr>
                        <td>Anom</td>
                        <td>19</td>
                        <td>Male</td>
                    </tr>
                    <tr>
                        <td>Megha</td>
                        <td>19</td>
                        <td>Female</td>
                    </tr>
                    <tr>
                        <td>Subham</td>
                        <td>25</td>
                        <td>Male</td>
                    </tr>
                </table>
            </div>
        )
    }
}
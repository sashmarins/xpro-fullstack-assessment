import React from "react";
import CompanyDropdown from "./companyDropdown";

export default class Sidebar extends React.Component {

    render () {
        return(
            <div className="Sidebar">
                <h1> Meshuggah </h1>
                <CompanyDropdown/>
            </div>
        )
    }
}
import React from "react";

export default class CompanyDropdown extends React.Component {
    render () {
        return(
            <div className="companies">
                <a className="companyHeader">
                    <button className="headerbtn"> 
                    <b> Companies </b> 
                    </button>
                    <div class="companies-content">
                        <a>Meshuggah &#9660; </a>
                        <div className="meshuggah-content">
                            <a href="#">Users List</a>
                        </div>
                        <hr></hr>
                        <a>Animals As Leaders &#9660; </a>
                        <div className="AAL-content">
                            <a href="#">Users List</a>
                        </div>
                    </div>
                </a>
            </div>
        )
    }
}
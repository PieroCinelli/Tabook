import React from "react";
import ReservationForm from "./components/ReservationForm";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import logo from './logo.png';

const App = () => {
    return (
        <div>
            <div className="text-center mb-4">
                <img src={logo} alt="Tabook Logo" className="logo" />
            </div>
            <ReservationForm />
        </div>
    );
};

export default App;

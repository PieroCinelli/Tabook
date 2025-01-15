import React from "react";
import ReservationForm from "./components/ReservationForm";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

const App = () => {
    return (
        <div>
            <h1 className="text-center mt-3">Tabook</h1>
            <ReservationForm />
        </div>
    );
};

export default App;

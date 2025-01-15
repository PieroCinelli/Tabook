import React, { useState } from "react";
import axios from "axios";

const ReservationForm = () => {
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        date: "",
        time: "",
        num_people: "",
    });

    const [successMessage, setSuccessMessage] = useState("");

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post("http://127.0.0.1:8000/api/reservations/", formData);
            setSuccessMessage("Prenotazione effettuata con successo!");
            setFormData({
                name: "",
                email: "",
                date: "",
                time: "",
                num_people: "",
            });
        } catch (error) {
            console.error("Errore durante l'invio della prenotazione:", error);
        }
    };

    return (
        <div className="container mt-5">
            <h2 className="text-center mb-4">Prenota un Tavolo</h2>
            {successMessage && <div className="alert alert-success">{successMessage}</div>}
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="name" className="form-label">Nome</label>
                    <input
                        type="text"
                        className="form-control"
                        id="name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        placeholder="Inserisci il tuo nome"
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        placeholder="Inserisci la tua email"
                        required
                    />
                </div>
                <div className="row">
                    <div className="col-md-6 mb-3">
                        <label htmlFor="date" className="form-label">Data</label>
                        <input
                            type="date"
                            className="form-control"
                            id="date"
                            name="date"
                            value={formData.date}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="col-md-6 mb-3">
                        <label htmlFor="time" className="form-label">Orario</label>
                        <input
                            type="time"
                            className="form-control"
                            id="time"
                            name="time"
                            value={formData.time}
                            onChange={handleChange}
                            required
                        />
                    </div>
                </div>
                <div className="mb-3">
                    <label htmlFor="num_people" className="form-label">Numero di Persone</label>
                    <input
                        type="number"
                        className="form-control"
                        id="num_people"
                        name="num_people"
                        value={formData.num_people}
                        onChange={handleChange}
                        min="1"
                        placeholder="Quante persone?"
                        required
                    />
                </div>
                <button type="submit" className="btn btn-primary w-100">Invia Prenotazione</button>
            </form>
        </div>
    );
};

export default ReservationForm;

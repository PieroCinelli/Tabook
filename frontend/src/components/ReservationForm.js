import React, { useState } from 'react';
import axios from 'axios';

const ReservationForm = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [numPeople, setNumPeople] = useState(1);
  const [phoneNumber, setPhoneNumber] = useState('');
  const [availableTimes, setAvailableTimes] = useState([
    { start: '12:00', end: '14:30' },
    { start: '19:30', end: '21:30' }
  ]); // Fasce orarie disponibili
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [maxPeopleLimit, setMaxPeopleLimit] = useState(4); // Limite massimo delle persone per prenotazione
  const [invalidTimeMessage, setInvalidTimeMessage] = useState('');

  // Funzione per verificare se l'orario inserito è valido rispetto alle fasce orarie
  const isTimeInRange = (time, range) => {
    console.log('Verificando orario:', time); // Log dell'orario inserito
    const [startHour, startMinute] = range.start.split(':').map(Number);
    const [endHour, endMinute] = range.end.split(':').map(Number);
    const [inputHour, inputMinute] = time.split(':').map(Number);

    const startTime = new Date(2022, 0, 1, startHour, startMinute);
    const endTime = new Date(2022, 0, 1, endHour, endMinute);
    const inputTime = new Date(2022, 0, 1, inputHour, inputMinute);

    console.log('Start time:', startTime, 'End time:', endTime, 'Input time:', inputTime); // Log dei tempi per il debug
    return inputTime >= startTime && inputTime <= endTime;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Verifica se l'orario inserito è valido rispetto alle fasce orarie
    const validTime = availableTimes.some((range) => isTimeInRange(time, range));
    if (!validTime) {
      setInvalidTimeMessage(`Gli orari disponibili sono: ${availableTimes.map(range => `${range.start} - ${range.end}`).join(', ')}`);
      setSuccessMessage('');
      return;
    }

    // Verifica se il numero di persone supera il limite massimo
    if (numPeople > maxPeopleLimit) {
      setErrorMessage(`Il numero di persone non può superare ${maxPeopleLimit}`);
      setSuccessMessage('');
      return;
    }

    const reservationData = {
      name,
      email,
      date,
      time,
      num_people: numPeople,
      phone_number: phoneNumber,
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/reservations/', reservationData);
      setSuccessMessage('Prenotazione inviata con successo!');
      setErrorMessage('');
      setInvalidTimeMessage('');
    } catch (error) {
      setErrorMessage('Si è verificato un errore, riprova!');
      setSuccessMessage('');
      setInvalidTimeMessage('');
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Prenota il tuo Tavolo</h2>
      <form onSubmit={handleSubmit} className="bg-light p-4 rounded shadow-sm">
        <div className="mb-3">
          <label htmlFor="name" className="form-label">Nome</label>
          <input
            type="text"
            id="name"
            className="form-control"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email</label>
          <input
            type="email"
            id="email"
            className="form-control"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="date" className="form-label">Data</label>
          <input
            type="date"
            id="date"
            className="form-control"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="time" className="form-label">Orario</label>
          <input
            type="time"
            id="time"
            className="form-control"
            value={time}
            onChange={(e) => setTime(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="numPeople" className="form-label">Numero di persone</label>
          <input
            type="number"
            id="numPeople"
            className="form-control"
            value={numPeople}
            onChange={(e) => setNumPeople(e.target.value)}
            min="1"
            max={maxPeopleLimit} // Imposta il limite massimo delle persone
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="phoneNumber" className="form-label">Numero di telefono</label>
          <input
            type="tel"
            id="phoneNumber"
            className="form-control"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
            required
            placeholder="Es: +390000000000"
          />
        </div>

        <button type="submit" className="btn btn-primary w-100">Invia Prenotazione</button>
      </form>

      {successMessage && <div className="alert alert-success mt-3">{successMessage}</div>}
      {errorMessage && <div className="alert alert-danger mt-3">{errorMessage}</div>}
      {invalidTimeMessage && <div className="alert alert-warning mt-3">{invalidTimeMessage}</div>}
    </div>
  );
};

export default ReservationForm;

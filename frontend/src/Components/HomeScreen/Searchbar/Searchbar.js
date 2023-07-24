import { AppBar, Toolbar, TextField, Button, Autocomplete } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import fetchHotels from '../../../api/endpoints/hotels';
import fetchCities from '../../../api/endpoints/cities';
import { useState, useEffect } from 'react';

const Searchbar = () => {

    const [cities, setCities] = useState([]);
    const [selectedCity, setSelectedCity] = useState('');
    const [numberOfDays, setNumberOfDays] = useState(null);
    const [hotels, setHotels] = useState([]);
    const [selectedHotel, setSelectedHotel] = useState('');

    const navigate = useNavigate()

    const handleOnClick = () => {
      if (!selectedCity || !selectedHotel || !numberOfDays) {
        alert('Please fill in all required fields.');
        return;
      }

      const queryParams = new URLSearchParams();
      queryParams.append('city', selectedCity);
      queryParams.append('days', numberOfDays);
      queryParams.append('hotel', selectedHotel);
      //history.push(`/next-page?${queryParams.toString()}`);
      navigate(`/interests?${queryParams.toString()}`)
    }

    const handleCityChange = (event, value) => {
      setSelectedCity(value);
    };

    const handleDaysChange = (event) => {
      setNumberOfDays(event.target.value);
    }

    const handleHotelChange = (event, value) => {
      if (selectedCity)
            setSelectedHotel(value)
      
    }

    useEffect(() => {
      fetchCities()
        .then(data => {
          setCities(data)
        }).then(() => {
          console.log(selectedCity)
        fetchHotels(selectedCity).then(data =>
          setHotels(data)
        )
        })
    }, [selectedCity]);

    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <AppBar
          position="absolute"
          sx={{
            top: '20%',
            left: '10%',
            //transform: 'translate(-50%, 20%)',
            width: '80%',
            background: 'linear-gradient(0deg, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)), #CDCDDF',
            borderRadius: '50px',
            //height: '6.5vh'
          }}
        >
          <Toolbar>
            <div style={{ display: 'flex', width: '100%', paddingTop: '5px' }}>
              
              <Autocomplete
                value={selectedCity}
                onChange={handleCityChange}
                options={cities}
                getOptionLabel={(city) =>  city || ""}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    label={!(cities && cities.length) ? "City (Loading data..)" : "City"}
                    variant="standard"
                    InputProps={{
                      ...params.InputProps,
                      style: { fontSize: '2.2vh' },
                      required: true
                    }}
                    InputLabelProps={{ 
                      ...params.InputLabelProps,
                      style: { fontSize: '1.8vh' } }}
                  />
                )} 
                freeSolo
                renderOption={(props, option) => (
                  <li {...props} style={{ fontSize: '1.8vh' }}>
                    {option}
                  </li>
                )}
                sx={{ flex: 1, marginRight: '10px' }}
                disabled={!(cities && cities.length)}
              />
              <TextField
                label="Number of Days"
                variant="standard"
                inputProps={{ style: { fontSize: '2.2vh' } }}
                InputLabelProps={{ style: { fontSize: '1.8vh' } }}
                style={{ flex: 1, marginRight: '10px' }}
                onChange={handleDaysChange}
                value = {numberOfDays}
              />
              <Autocomplete
                value={selectedHotel}
                onChange={handleHotelChange}
                options={hotels}
                getOptionLabel={(hotel) =>  hotel || ""}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    label={selectedCity ? "Hotel Name" : "Hotel Name(Select a City)" }
                    variant="standard"
                    InputProps={{
                      ...params.InputProps,
                      style: { fontSize: '2.2vh' },
                      required: true
                    }}
                    InputLabelProps={{ 
                      ...params.InputLabelProps,
                      style: { fontSize: '1.8vh' } }}
                  />
                )} 
                disabled={!selectedCity}
                freeSolo
                renderOption={(props, option) => (
                  <li {...props} style={{ fontSize: '2vh' }}>
                    {option}
                  </li>
                )}
                sx={{ flex: 1, marginRight: '10px' }}
              />
            </div>
          </Toolbar>
        </AppBar>
        
        <Button variant="contained" color="primary" size="large" 
        sx={{
             position : 'absolute',
             top:'30%',
             backgroundColor:"#3B3A4C",
             '&:hover': {
              backgroundColor: '#5E5F71', // Button color on hover
            },
             fontSize: '1.8vh'}}
             onClick={handleOnClick}>
          Start
        </Button>
     
    </div>
    
        
    );
}

export default Searchbar;

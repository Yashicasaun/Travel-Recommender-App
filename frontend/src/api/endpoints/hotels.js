const fetchHotels = (city) => {
    //return fetch(`https://travel-recommender-flask.onrender.com/api/hotels?city=${encodeURIComponent(city)}`)
    return fetch(`http://127.0.0.1:5000/api/hotels?city=${encodeURIComponent(city)}`)
      .then(response => response.json())
      .then(data => data)
      .catch(error => {
        console.error("errordgfg",error);
        return [];
      });
  };
  
  export default fetchHotels;
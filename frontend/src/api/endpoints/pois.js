const fetchPois = (city, categories) => {
    //return fetch(`https://travel-recommender-flask.onrender.com/api/pois?city=${encodeURIComponent(city)}&categories=${encodeURIComponent(categories)}`)
    return fetch(`http://127.0.0.1:5000/api/pois?city=${encodeURIComponent(city)}&categories=${encodeURIComponent(categories)}`)  
      .then(response => response.json())
      .then(data => data)
      .catch(error => {
        console.error(error);
        return [];
      });
  };
  
  export default fetchPois;
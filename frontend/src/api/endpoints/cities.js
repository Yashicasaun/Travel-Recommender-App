const fetchCities = () => {

    //return ['Munich', 'London']
    //return fetch('https://travel-recommender-flask.onrender.com/api/cities')
    return fetch('http://127.0.0.1:5000/api/cities')
      .then(response => response.json())
      .then(data => data)
      .catch(error => {
        console.error(error);
        return [];
      });
  };
  
  export default fetchCities;
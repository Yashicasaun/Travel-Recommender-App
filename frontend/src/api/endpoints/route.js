const fetchRoutes = (params) => {
  //return fetch(`https://travel-recommender-flask.onrender.com/api/routes?params=${encodeURIComponent(params)}`)
  return fetch(`http://127.0.0.1:5000/api/routes?params=${encodeURIComponent(params)}`) 
    
  .then((response) => response.json())
    .then((data) => data)
    .catch((error) => {
      console.error(error);
      return [];
    });
  //return Promise.resolve(routes)
};

export default fetchRoutes;
const fetchCategories = (city) => {
  //return fetch(`https://travel-recommender-flask.onrender.com/api/categories?city=${encodeURIComponent(city)}`)
  return fetch(`http://127.0.0.1:5000/api/categories?city=${encodeURIComponent(city)}`)
    .then((response) => response.json())
    .then((data) => data)
    .catch((error) => {
      console.error(error);
      return [];
    });
};

const fetchSubcategories = (city) => {
  return (
    // fetch(
    //   `https://travel-recommender-flask.onrender.com/api/subcategories?city=${encodeURIComponent(
    //     city
    //   )}`
    // )
    fetch(`http://127.0.0.1:5000/api/subcategories?city=${encodeURIComponent(city)}`)
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => {
        console.error(error);
        return [];
      })
  );
};

export { fetchCategories, fetchSubcategories };

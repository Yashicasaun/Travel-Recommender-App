import React, { useState } from "react";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  Polyline,
} from "react-leaflet";
import styles from "./InterestsScreen.module.css";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { ChevronLeft, ChevronRight } from "@mui/icons-material";
import { Icon } from "leaflet";
import { Select, MenuItem, Typography } from "@mui/material";

function CreateRoute() {
  // const [routes, setRoutes] = useState({})

  //const location = useLocation();

  //const queryParams = new URLSearchParams(location.search);
  const routes = {
    "Ant Colony Optimization (ACO)": {
      "Day 0": [
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
        { name: "Deutsches Museum", value: [48.129902, 11.583512] },
        { name: "Englischer Garten", value: [48.151673, 11.592511] },
        {
          name: "Nymphenburg Palace (Schloss Nymphenburg)",
          value: [48.158311, 11.503469],
        },
        { name: "Olympiaberg", value: [48.16976, 11.551545] },
        { name: "Olympia-Reitanlagen GmbH", value: [48.142882, 11.66612] },
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
      ],
      "Day 1": [
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
        { name: "Marienplatz", value: [48.137262, 11.575096] },
        { name: "Hofgarten", value: [48.142925, 11.580047] },
        { name: "Dianatempel", value: [48.142975, 11.579994] },
        { name: "Siegestor", value: [48.152338, 11.582115] },
        { name: "Dem Bayerischen Heere", value: [48.152417, 11.582035] },
        { name: "Ehrenhof", value: [48.158272, 11.504344] },
        { name: "Pinakothek der Moderne", value: [48.14719, 11.572348] },
        { name: "Hinterbrühler See", value: [48.085239, 11.54218] },
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
      ],
      "Day 2": [
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
        { name: "Karlsplatz", value: [48.139069, 11.565978] },
        { name: "Alte Pinakothek", value: [48.148327, 11.569776] },
        { name: "Olympic Park (Olympiapark)", value: [48.173886, 11.54555] },
        { name: "Bayerische Staatsoper", value: [48.139615, 11.579334] },
        { name: "Bayerische Staatskanzlei", value: [48.142277, 11.58272] },
        { name: "Sub", value: [48.132549, 11.573495] },
        { name: "Flauchersteg", value: [48.107446, 11.55736] },
        { name: "Flaucher", value: [48.109513, 11.557848] },
        { name: "Tierpark Hellabrunn", value: [48.09749, 11.554018] },
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
      ],
    },
    // "Iterated Local Search (ILS)": {
    //   "Day 0": {
    //     "Bayerische Staatskanzlei": [48.142277, 11.58272],
    //     Marienplatz: [48.137262, 11.575096],
    //     "Nymphenburg Palace (Schloss Nymphenburg)": [48.158311, 11.503469],
    //     Ehrenhof: [48.158272, 11.504344],
    //     Marstallmuseum: [48.15608, 11.50566],
    //     "Nymphenburger Kanal": [48.158724, 11.51708],
    //     "Eisbach Wave (Eisbachwelle)": [48.143474, 11.587886],
    //     "House of Art (Haus der Kunst)": [48.144068, 11.585896],
    //     "Wasserfall im Englischen Garten": [48.14514, 11.587347],
    //     Hofgarten: [48.142925, 11.580047],
    //     Dianatempel: [48.142975, 11.579994],
    //     "Bayerische Staatsoper": [48.139615, 11.579334],
    //     Nationaltheater: [48.139566, 11.579386],
    //     "Max-Joseph-Platz": [48.139852, 11.578247],
    //   },
    //   "Day 1": {
    //     "Alte Pinakothek": [48.148327, 11.569776],
    //     "Staatliches Museum Ägyptischer Kunst": [48.147206, 11.568378],
    //     "Paläontologisches Museum": [48.147529, 11.563557],
    //     "Städtische Galerie im Lenbachhaus": [48.14676, 11.563966],
    //     Königsplatz: [48.145951, 11.56525],
    //     Glyptothek: [48.146532, 11.565791],
    //     Luitpoldpark: [48.172595, 11.57036],
    //     "SEA LIFE München": [48.173824, 11.556359],
    //     "Olympiapark SoccaFive Arena": [48.17497, 11.55615],
    //     "Olympia-Eisstadion": [48.175093, 11.557058],
    //     "BMW Museum": [48.176781, 11.558889],
    //     Olympiaberg: [48.16976, 11.551545],
    //     Olympiahalle: [48.174927, 11.550053],
    //     "Olympic Park (Olympiapark)": [48.173886, 11.54555],
    //     "Wiener Platz": [48.133893, 11.593795],
    //   },
    //   "Day 2": {
    //     "Deutsches Jagd- und Fischereimuseum": [48.138359, 11.571318],
    //     "St. Michael's Church (St. Michael)": [48.138546, 11.570284],
    //     "Denkmal-fuer-Michael-Jackson": [48.140281, 11.573416],
    //     "Kunsthalle München": [48.140042, 11.575858],
    //     "New Town Hall (Neues Rathaus)": [48.137582, 11.575793],
    //     Rindermarkt: [48.13617, 11.574083],
    //     "Deutsches Museum": [48.129902, 11.583512],
    //     Reichenbachbrücke: [48.127371, 11.576969],
    //     "Isarufer an der Reichenbachbrücke": [48.126804, 11.576537],
    //     "Dem Bayerischen Heere": [48.152417, 11.582035],
    //     Siegestor: [48.152338, 11.582115],
    //     Monopteros: [48.149863, 11.590922],
    //     "Englischer Garten": [48.151673, 11.592511],
    //     Corneliusbrücke: [48.128364, 11.580169],
    //   },
    // },
    "Greedy Randomized Adaptive Search Procedures": {
      "Day 0": [
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
        {
          name: "Botanischer Garten München-Nymphenburg (Botanischer Garten)",
          value: [48.162651, 11.500261],
        },
        { name: "Gewächshäuser", value: [48.163716, 11.501614] },
        { name: "Reichenbachbrücke", value: [48.127371, 11.576969] },
        {
          name: "Isarufer an der Reichenbachbrücke",
          value: [48.126804, 11.576537],
        },
        { name: "Karlsplatz", value: [48.139069, 11.565978] },
        {
          name: "Nymphenburg Palace (Schloss Nymphenburg)",
          value: [48.158311, 11.503469],
        },
        { name: "Nymphenburger Kanal", value: [48.158724, 11.51708] },
        { name: "Corneliusbrücke", value: [48.128364, 11.580169] },
        {
          name: "Staatstheater am Gärtnerplatz",
          value: [48.131284, 11.575788],
        },
        { name: "Kunsthalle München", value: [48.140042, 11.575858] },
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
      ],
      "Day 1": [
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
        { name: "Galerie Hegemann", value: [48.135924, 11.570186] },
        { name: "Rindermarkt", value: [48.13617, 11.574083] },
        { name: "Marienplatz", value: [48.137262, 11.575096] },
        {
          name: "New Town Hall (Neues Rathaus)",
          value: [48.137582, 11.575793],
        },
        { name: "Denkmal-fuer-Michael-Jackson", value: [48.140281, 11.573416] },
        { name: "Antiquarium", value: [48.140547, 11.578958] },
        { name: "Max-Joseph-Platz", value: [48.139852, 11.578247] },
        { name: "Bayerische Staatsoper", value: [48.139615, 11.579334] },
        { name: "Nationaltheater", value: [48.139566, 11.579386] },
        {
          name: "St. Michael's Church (St. Michael)",
          value: [48.138546, 11.570284],
        },
        { name: "Deutsches Museum", value: [48.129902, 11.583512] },
        { name: "Wiener Platz", value: [48.133893, 11.593795] },
        { name: "Dianatempel", value: [48.142975, 11.579994] },
        { name: "Hofgarten", value: [48.142925, 11.580047] },
        { name: "Eisbach Wave (Eisbachwelle)", value: [48.143474, 11.587886] },
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
      ],
      "Day 2": [
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
        { name: "Olympic Park (Olympiapark)", value: [48.173886, 11.54555] },
        { name: "Olympiahalle", value: [48.174927, 11.550053] },
        { name: "BMW Museum", value: [48.176781, 11.558889] },
        { name: "Luitpoldpark", value: [48.172595, 11.57036] },
        { name: "Paläontologisches Museum", value: [48.147529, 11.563557] },
        { name: "Königsplatz", value: [48.145951, 11.56525] },
        { name: "Glyptothek", value: [48.146532, 11.565791] },
        {
          name: "Staatliches Museum Ägyptischer Kunst",
          value: [48.147206, 11.568378],
        },
        { name: "Alte Pinakothek", value: [48.148327, 11.569776] },
        { name: "Museum Brandhorst", value: [48.148144, 11.574342] },
        { name: "Dem Bayerischen Heere", value: [48.152417, 11.582035] },
        { name: "Siegestor", value: [48.152338, 11.582115] },
        { name: "Englischer Garten", value: [48.151673, 11.592511] },
        {
          name: "Holiday Inn München - Zentrum",
          value: [48.130642, 11.589687],
        },
      ],
    },
    // "Simulated Annealing and Iterated Local Search (SAILS)": {
    //   "Day 0": {
    //     "Deutsches Museum": [48.129902, 11.583512],
    //     Corneliusbrücke: [48.128364, 11.580169],
    //     Reichenbachbrücke: [48.127371, 11.576969],
    //     "Isarufer an der Reichenbachbrücke": [48.126804, 11.576537],
    //     "Wiener Platz": [48.133893, 11.593795],
    //     "SEA LIFE München": [48.173824, 11.556359],
    //     "Olympiapark SoccaFive Arena": [48.17497, 11.55615],
    //     "Olympia-Eisstadion": [48.175093, 11.557058],
    //     "BMW Museum": [48.176781, 11.558889],
    //   },
    //   "Day 1": {
    //     "Kunsthalle München": [48.140042, 11.575858],
    //     "New Town Hall (Neues Rathaus)": [48.137582, 11.575793],
    //     Marienplatz: [48.137262, 11.575096],
    //     Rindermarkt: [48.13617, 11.574083],
    //     "Jüdisches Museum München": [48.134375, 11.572263],
    //     "Galerie Hegemann": [48.135924, 11.570186],
    //     "St. Michael's Church (St. Michael)": [48.138546, 11.570284],
    //     "Deutsches Jagd- und Fischereimuseum": [48.138359, 11.571318],
    //     "Bayerische Staatsoper": [48.139615, 11.579334],
    //     "Max-Joseph-Platz": [48.139852, 11.578247],
    //     "Denkmal-fuer-Michael-Jackson": [48.140281, 11.573416],
    //     Nationaltheater: [48.139566, 11.579386],
    //     Antiquarium: [48.140547, 11.578958],
    //     "Cuvilliés-Theater": [48.14125, 11.577684],
    //   },
    //   "Day 2": {
    //     "Wasserfall im Englischen Garten": [48.14514, 11.587347],
    //     "House of Art (Haus der Kunst)": [48.144068, 11.585896],
    //     "Englischer Garten": [48.151673, 11.592511],
    //     "Nymphenburger Kanal": [48.158724, 11.51708],
    //     Marstallmuseum: [48.15608, 11.50566],
    //     Ehrenhof: [48.158272, 11.504344],
    //     "Nymphenburg Palace (Schloss Nymphenburg)": [48.158311, 11.503469],
    //     "Eisbach Wave (Eisbachwelle)": [48.143474, 11.587886],
    //     Luitpoldpark: [48.172595, 11.57036],
    //     Olympiaberg: [48.16976, 11.551545],
    //     "Olympic Park (Olympiapark)": [48.173886, 11.54555],
    //     Olympiahalle: [48.174927, 11.550053],
    //   },
    // },
  };

  const [selectedAlgorithm, setSelectedAlgorithm] = useState(
    Object.keys(routes)[0]
  );
  const handleAlgorithmChange = (event) => {
    setSelectedAlgorithm(event.target.value);
  };

  const circleIcon = new Icon({
    iconUrl: require("./circle.svg").default, // Add the URL or path to your circle icon image here
    iconSize: [12, 12], // Adjust the size of the icon as per your requirement
    iconAnchor: [6, 6], // Adjust the anchor point of the icon as per your requirement
  });

  const handleSliderChange = (index) => {
    setSelectedDayIndex(Object.keys(routes[selectedAlgorithm])[index]);
  };

  const [selectedDayIndex, setSelectedDayIndex] = useState("Day 0");

  const sliderSettings = {
    dots: true,
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    speed: 500,
    prevArrow: <CustomPrevArrow />,
    nextArrow: <CustomNextArrow />,
    afterChange: handleSliderChange,
  };
  function CustomPrevArrow(props) {
    const { onClick } = props;

    return (
      <div className={styles.customPrevArrow} onClick={onClick}>
        <div className={styles.arrowCircle}>
          <ChevronLeft className={styles.arrowIcon} />
        </div>
      </div>
    );
  }

  function CustomNextArrow(props) {
    const { onClick } = props;
    return (
      <div className={styles.customNextArrow} onClick={onClick}>
        <div className={styles.arrowCircle}>
          <ChevronRight className={styles.arrowIcon} />
        </div>
      </div>
    );
  }

  //const defaultCenter = [48.1351, 11.582];
  //const defaultZoom = 14;

  //const colors = ["red", "blue", "black"]; // Array of colors for paths

  return (
    <div className={styles.InterestsScreen}>
      {Object.entries(routes).length > 0 ? (
        <div
          style={{
            marginTop: "15vh",
            marginBottom: "2vh",
            marginLeft: "5vw",
            height: "70vh",
            width: "60vw",
          }}
        >
          <Select
            value={selectedAlgorithm}
            onChange={handleAlgorithmChange}
            style={{ fontSize: "2vh", marginBottom: "2vh", minWidth: "0px" }}
          >
            {Object.entries(routes).map(
              ([algorithmName, algorithmData], algorithmIndex) => (
                <MenuItem key={algorithmName} value={algorithmName}>
                  <Typography variant="body1">{algorithmName}</Typography>
                </MenuItem>
              )
            )}
          </Select>
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <div style={{ minWidth: "0px", marginRight: "3vw" }}>
              <Slider {...sliderSettings}>
                {Object.entries(routes[selectedAlgorithm]).map(
                  ([day, places], dayIndex) => {
                    const coordinates = places.map((item) => item.value);
                    const bounds = coordinates.reduce((bounds, coordinate) => {
                      console.log("Current Coordinate:", coordinates[0][0]); // Log current coordinate
                      return bounds.extend(coordinate);
                    }, L.latLngBounds(coordinates[0], coordinates[0]));
                    const center = bounds.getCenter();
                    const zoom = calculateZoomLevel(bounds);

                    return (
                      <div key={day}>
                        <MapContainer
                          center={center}
                          zoom={zoom}
                          style={{ height: "70vh", width: "60vw" }}
                        >
                          <TileLayer
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            opacity={0.7}
                          />
                          <Polyline
                            positions={coordinates}
                            color="#6E6D73"
                            weight={3}
                          />
                          {Object.entries(places).map(({ name, value }) => (
                            <Marker
                              key={name}
                              position={value}
                              icon={circleIcon}
                            >
                              <Popup>{name}</Popup>
                            </Marker>
                          ))}
                        </MapContainer>
                      </div>
                    );
                  }
                )}
              </Slider>
            </div>
            <div style={{ minWidth: "0px" }}>
              {Object.entries(routes[selectedAlgorithm][selectedDayIndex]).map(
                ([place]) => (
                  <div key={place}>
                    <h3>{place}</h3>
                  </div>
                )
              )}
            </div>
          </div>
        </div>
      ) : (
        <p>Loading routes...</p>
      )}
    </div>
  );
}

function calculateZoomLevel(bounds) {
  const WORLD_DIM = { height: 256, width: 256 };
  const ZOOM_MAX = 16;

  const ne = bounds.getNorthEast();
  const sw = bounds.getSouthWest();

  const latFraction = (Math.abs(ne.lat - sw.lat) / 180) * WORLD_DIM.height;
  const lngFraction = (Math.abs(ne.lng - sw.lng) / 360) * WORLD_DIM.width;

  const latZoom = Math.ceil(Math.log2(WORLD_DIM.height / latFraction));
  const lngZoom = Math.ceil(Math.log2(WORLD_DIM.width / lngFraction));

  return Math.min(ZOOM_MAX, Math.min(latZoom, lngZoom));
}

export default CreateRoute;

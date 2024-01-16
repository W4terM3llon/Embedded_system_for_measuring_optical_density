import {
  Box,
  Button,
  Container,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
} from "@mui/material";
import { useState, useEffect, useMemo } from "react";
import { blob } from "stream/consumers";
import downloadSvg from '../public/download-svgrepo-com.svg'

export function StaticImagePage() {
  const [data, setData] = useState<any>(null);
  const [isLoading, setLoading] = useState<any>(true);

  const [measurementId, setMeasurementId] = useState<number>(1);

  useEffect(() => {
    fetch(
      "http://127.0.0.1:5000/api/v1/yeastGrowthPlot?" +
        new URLSearchParams({ id: `${measurementId}` }),
      {
        method: "GET",
      }
    )
      .then((response) => response.blob())
      .then((blob) => {
        setData(blob);
        setLoading(false);
      })
      .catch((x) => console.log(x));
  }, [measurementId]);

  const url = useMemo(() => (data ? URL.createObjectURL(data) : ""), [data]);

  /*
useEffect(() => {
    fetch("http://127.0.0.1:5000/api/v1/hello", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: JSON.stringify({"growthIntensity": new Date().getTime()%100000 / 1000, "dateTime":  new Date().toISOString()})
    })
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((x) => console.log(x));
  }, []);
*/

  if (isLoading) return <p>Loading...</p>;
  if (!data) return <p>No profile data</p>;

  return (
    <Container
      sx={{
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Container
        sx={{ display: "flex", flexDirection: "column", alignItems: "center" }}
      >
        <Box sx={{ height: "600px", width: "600px", display: "flex" }}>
          <img
            style={{ height: "100%", width: "100%", objectFit: "contain" }}
            src={`${url}`}
          ></img>
        </Box>
        <FormControl  variant="standard" fullWidth sx={{width: "600px"}}>
          <Container
            sx={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: 'center',
              width: "100%",
            }}
          >
            <div></div>
            <div>
              <Select
                labelId="Measurement-label"
                id="Measurement"
                value={measurementId}
                label="Measurement"
                onChange={(e) => {
                  setMeasurementId(e.target.value as number);
                }}
              >
                <MenuItem value={1}>1st measurement (1 day)</MenuItem>
                <MenuItem value={2}>2nd measurement (3 days)</MenuItem>
                <MenuItem value={3}>3rd measurement (1 day)</MenuItem>
              </Select>
            </div>
            <div>
              <a href={"http://127.0.0.1:5000/api/v1/yeastGrowthPlot?" + new URLSearchParams({ id: `${measurementId}` })}>
              <img
                style={{ height: "2rem", width: "2rem", objectFit: "contain"}}
                src={downloadSvg.src}
              />
              </a>
            </div>
          </Container>
        </FormControl>
      </Container>
    </Container>
  );
}

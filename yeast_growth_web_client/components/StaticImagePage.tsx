import {
  Box,
  Button,
  Container,
  FormControl,
  FormControlLabel,
  FormLabel,
  InputLabel,
  MenuItem,
  Select,
  Switch,
} from "@mui/material";
import { useState, useEffect, useMemo, useCallback } from "react";
import { blob } from "stream/consumers";
import downloadSvg from "../public/download-svgrepo-com.svg";

const env = process.env.NODE_ENV
const hostAddress = env == "production" ? '192.168.195.204' : 'localhost';

export function StaticImagePage() {
  const [measurementFileNames, setMeasurementFileNames] = useState<string[]>(
    []
  );
  const [data, setData] = useState<any>(null);
  const [isLoading, setLoading] = useState<any>(true);
  const [isAutoUpdate, setIsAutoUpdate] = useState<boolean>(false);
  const [chosenMeasurementFileName, setChosenMeasurementFileName] =
    useState<string>("");

  const [count, setCount] = useState(0);

  const fetchData = useCallback((measurementFileName: string) => {
    fetch(
      `http://${hostAddress}:5000/api/v1/yeastGrowthPlot?` +
        new URLSearchParams({ id: measurementFileName }),
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
  }, []);

  useEffect(() => {
    const timer = setTimeout(() => {
      setCount(count + 1);
      if (isAutoUpdate && chosenMeasurementFileName) {
        fetchData(chosenMeasurementFileName);
      }
    }, 1000);
    return () => clearTimeout(timer);
  }, [chosenMeasurementFileName, count, fetchData, isAutoUpdate]);

  const onFileNameChosen = useCallback(
    (measurementFileName: string) => {
      setChosenMeasurementFileName(measurementFileName);
      fetchData(measurementFileName);
    },
    [fetchData]
  );

  useEffect(() => {
    fetch(`http://${hostAddress}:5000/api/v1/measurementFileNames`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setMeasurementFileNames(data.measurementFileNames);
        if (data.measurementFileNames.length > 0) {
          onFileNameChosen(data.measurementFileNames[0]);
        }
      })
      .catch((x) => console.log(x));
  }, [onFileNameChosen]);

  const url = useMemo(() => (data ? URL.createObjectURL(data) : ""), [data]);

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
        {!isLoading ? (
          <>
            <Box sx={{ height: {xs: '100%', lg: "600px"}, width: {xs: '100%', lg: "600px"}, display: "flex" }}>
              {url ? (
                <img
                  style={{
                    height: "100%",
                    width: "100%",
                    objectFit: "contain",
                  }}
                  src={`${url}`}
                />
              ) : (
                <p>Please choose a measurement</p>
              )}
            </Box>
            <FormControl variant="standard" sx={{ width: {xs: '100%', lg: "600px"} }}>
              <Container
                sx={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  width: "100%",
                  flexDirection: {xs: 'column', lg: 'row'},
                }}
              >
                <Container sx={{marginTop: {xs: '2rem', lg: '0rem'}}}>
                  <FormControlLabel
                    control={
                      <Switch
                        value={isAutoUpdate}
                        onChange={(e) => {
                          setIsAutoUpdate(e.target.checked);
                        }}
                      />
                    }
                    label="Auto update"
                  />
                </Container>
                <Container sx={{marginTop: {xs: '2rem', lg: '0rem'}}}>
                  <Select
                    labelId="Measurement-label"
                    id="Measurement"
                    value={chosenMeasurementFileName}
                    label="Measurement"
                    onChange={(e) => {
                      onFileNameChosen(e.target.value);
                    }}
                  >
                    {measurementFileNames.map((measurement) => (
                      <MenuItem key={measurement} value={measurement}>
                        {measurement}
                      </MenuItem>
                    ))}
                  </Select>
                </Container>
                <Container sx={{marginTop: {xs: '2rem', lg: '0rem'}}}>
                  <a
                    href={
                      `http://${hostAddress}:5000/api/v1/yeastGrowthPlot?` +
                      new URLSearchParams({ id: chosenMeasurementFileName })
                    }
                  >
                    <img
                      style={{
                        height: "2rem",
                        width: "2rem",
                        objectFit: "contain",
                      }}
                      src={downloadSvg.src}
                    />
                  </a>
                </Container>
              </Container>
            </FormControl>
          </>
        ) : (
          <p>Loading...</p>
        )}
      </Container>
    </Container>
  );
}

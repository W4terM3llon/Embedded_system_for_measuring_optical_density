import {
  Box,
  Button,
  Container,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
} from "@mui/material";
import { useState, useEffect, useMemo, useCallback } from "react";
import { blob } from "stream/consumers";
import downloadSvg from '../public/download-svgrepo-com.svg'

type MeasurementFileNamesType =
{
  measurementFileNames: string[];
}

export function StaticImagePage() {
  const [measurementFileNames, setMeasurementFileNames] = useState<string[]>([]);
  const [data, setData] = useState<any>(null);
  const [isLoading, setLoading] = useState<any>(true);

  const [chosenMeasurementFileName, setChosenMeasurementFileName] = useState<string>("");
  
  const onFileNameChosen = useCallback(
    (measurementFileName: string) => {
      setChosenMeasurementFileName(measurementFileName)

      fetch(
        "http://127.0.0.1:5000/api/v1/yeastGrowthPlot?" +
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
    },
    [],
  )
  
  useEffect(() => {
    fetch(
      "http://127.0.0.1:5000/api/v1/measurementFileNames",
      {
        method: "GET",
      }
    )
      .then((response) => response.json())
      .then((data) => {
        console.log(data)
        setMeasurementFileNames(data.measurementFileNames);
        if (data.measurementFileNames.length > 0)
        {
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
        {!isLoading ? (<><Box sx={{ height: "600px", width: "600px", display: "flex" }}>
          {url ? (<img
            style={{ height: "100%", width: "100%", objectFit: "contain" }}
            src={`${url}`} />) : (<p>Please choose a measurement</p>)}
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
                value={chosenMeasurementFileName}
                label="Measurement"
                onChange={(e) => {onFileNameChosen(e.target.value)}}
              >
                {measurementFileNames.map((measurement) => (<MenuItem key={measurement} value={measurement}>{measurement}</MenuItem>))}
              </Select>
            </div>
            <div>
              <a href={"http://127.0.0.1:5000/api/v1/yeastGrowthPlot?" + new URLSearchParams({ id: chosenMeasurementFileName })}>
              <img
                style={{ height: "2rem", width: "2rem", objectFit: "contain"}}
                src={downloadSvg.src}
              />
              </a>
            </div>
          </Container>
        </FormControl></>) : <p>Loading...</p>}
      </Container>
    </Container>
  );
}

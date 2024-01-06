import { Box, Container } from "@mui/material";
import { useState, useEffect, useMemo } from "react";
import { blob } from "stream/consumers";

export function StaticImagePage() {
  const [data, setData] = useState<any>(null);
  const [isLoading, setLoading] = useState<any>(true);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/v1/yeastGrowthPlot", {
      method: "GET",
    })
      .then((response) => response.blob())
      .then((blob) => {
        setData(blob);
        setLoading(false);
      })
      .catch((x) => console.log(x));
  }, []);

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
    <Container sx={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <Box sx={{ height: "600px", width: "600px", display: "flex"}}>
        <img style={{"height": "100%", "width": "100%", "objectFit": "contain"}} src={`${url}`}></img>
      </Box>
    </Container>
  );
}

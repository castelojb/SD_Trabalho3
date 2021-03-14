import React, { useState } from "react";
import SmartThingCard from "../../components/SmartThingCard";
import useService from "../../hooks/useService";
import { Button, Container } from "./styles";

const Home = () => {
  const [equipments, setEquipments] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState();
  const { getEquipments } = useService();
  return (
    <div>
      <p style={{ fontSize: "24px" }}>
        <b>Selecione o Produto</b>
      </p>
      <Button
        onClick={() => {
          getEquipments(setEquipments, setError, setLoading);
          setInterval(() => {
            getEquipments(setEquipments, setError, setLoading);
          }, [5000]);
        }}
      >
        Buscar nas proximidades
      </Button>
      <Container>
        {equipments.map(equipment => (
          <SmartThingCard
            key={equipment.id}
            id={equipment.id}
            name={equipment.name}
            status={equipment.status}
            type={equipment.type}
          />
        ))}
      </Container>
    </div>
  );
};

export default Home;

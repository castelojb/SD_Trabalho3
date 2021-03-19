import React, { useEffect, useState } from "react";
import { Card, Switch, InputNumber, Button, Progress } from "antd";
import useService from "../../hooks/useService";

const SmartThingCard = ({ id, name, type, status, subtype }) => {
  const [pageStatus, setPageStatus] = useState(status?.TURN_ON_OFF);
  const [value, setValue] = useState(
    status?.TEMPERATURE || status?.LIGHT_VALUE || status?.HAVE_SMOKE
  );
  let equipmentDetails = null;
  const { changeStatus } = useService();
  console.log(status);
  useEffect(() => {
    if (status?.TURN_ON_OFF !== undefined)
      setPageStatus(Number(status?.TURN_ON_OFF));
  }, [status]);

  useEffect(() => {
    if (pageStatus !== undefined) {
      changeStatus(
        id,
        Number(pageStatus),
        "TURN_ON_OFF",
        () => {},
        () => {},
        () => {}
      );
    }
  }, [pageStatus, changeStatus, id]);

  const SaveValue = () => {
    changeStatus(
      id,
      value,
      "VALUE",
      () => {},
      () => {},
      () => {}
    );
  };

  const renderTemperature = () =>
    status.TEMPERATURE !== undefined && (
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-start",
        }}
      >
        <InputNumber value={value} onChange={setValue} />
        <Progress
          type='circle'
          percent={status.TEMPERATURE}
          format={percert => `${percert}°C`}
          width={80}
          size='small'
        />
      </div>
    );

  if (type === "ACTUATOR") {
    equipmentDetails = (
      <>
        <p>Atuador</p>
        {status.TURN_ON_OFF !== undefined && (
          <>
            <p>{`Equipamento está ${pageStatus ? "Ligado" : "Desligado"}`}</p>
          </>
        )}
        {renderTemperature()}
      </>
    );
  } else if (type === "SENSOR") {
    if (subtype) {
      equipmentDetails = (
        <>
          <p>Sensor {subtype}</p>
          {status.HAVE_SMOKE !== undefined && (
            <>
              <p>{`Tem Fumaça? ${status.HAVE_SMOKE ? "Sim" : "Não"}`}</p>
            </>
          )}
          {status.LIGHT_VALUE !== undefined && (
            <Progress
              type='circle'
              percent={status.LIGHT_VALUE}
              format={percert => `${percert} de luminosidade`}
              width={80}
              size='small'
            />
          )}
          {status.TEMPERATURE !== undefined && (
            <Progress
              type='circle'
              percent={status.TEMPERATURE}
              format={percert => `${percert}°C`}
              width={80}
              size='small'
            />
          )}
        </>
      );
    }
  }

  return (
    <Card
      extra={
        status.TURN_ON_OFF !== undefined &&
        type !== "SENSOR" && (
          <Switch
            checked={pageStatus}
            onChange={status => setPageStatus(Number(status))}
          />
        )
      }
      title={name}
      style={{
        width: 300,
        textAlign: "start",
        marginLeft: "20px",
        marginTop: "20px",
      }}
      actions={
        type !== "SENSOR" &&
        status.VALUE && [<Button onClick={SaveValue}>Salvar valor</Button>]
      }
    >
      {equipmentDetails}
    </Card>
  );
};

export default SmartThingCard;

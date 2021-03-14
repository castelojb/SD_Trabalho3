import React, { useEffect, useState } from "react";
import { Card, Switch, InputNumber, Button, Progress } from "antd";
import useService from "../../hooks/useService";

const SmartThingCard = ({ id, name, type, status }) => {
  const [pageStatus, setPageStatus] = useState(status?.TURN_ON_OFF);
  const [temperature, setTemperature] = useState(status?.VALUE);
  let equipmentDetails = null;
  const { changeStatus } = useService();

  useEffect(() => {
    if (status?.TURN_ON_OFF !== undefined)
      setPageStatus(Number(status?.TURN_ON_OFF));
  }, [status]);

  useEffect(() => {
    if (pageStatus !== undefined) {
      console.log(pageStatus);
      changeStatus(
        id,
        Number(pageStatus),
        "TURN_ON_OFF",
        () => {},
        () => {},
        () => {}
      );
    }
  }, [pageStatus]);

  const SaveValue = () => {
    changeStatus(
      id,
      temperature,
      "VALUE",
      () => {},
      () => {},
      () => {}
    );
  };

  const renderEnvTemperature = () =>
    status.ENV_TEMPERATURE !== undefined && (
      <>
        <Progress
          type='circle'
          percent={status.ENV_TEMPERATURE}
          format={percert => `${percert}°C`}
          width={80}
          size='small'
        />
        <p>{`Temperatura no ambiente: ${status.ENV_TEMPERATURE}°C`}</p>
      </>
    );

  const renderTemperature = () =>
    status.VALUE !== undefined && (
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-start",
        }}
      >
        <InputNumber value={temperature} onChange={setTemperature} />
        <Progress
          type='circle'
          percent={status.VALUE}
          format={percert => `${percert}°C`}
          width={80}
          size='small'
        />
      </div>
    );

  if (type === "BOTH") {
    equipmentDetails = (
      <>
        <p>Sensor e atuador</p>
        {status.TURN_ON_OFF !== undefined && (
          <>
            <p>{`Equipamento está ${pageStatus ? "Ligado" : "Desligado"}`}</p>
          </>
        )}
        {status.VALUE !== undefined && (
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "flex-start",
            }}
          >
            {renderTemperature()}
            {renderEnvTemperature()}
          </div>
        )}
      </>
    );
  } else if (type === "ACTUATOR") {
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
    equipmentDetails = (
      <>
        <p>Sensor</p>
        <Progress
          type='circle'
          percent={status.VALUE}
          format={percert => `${percert}°C`}
          width={80}
          size='small'
        />
      </>
    );
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

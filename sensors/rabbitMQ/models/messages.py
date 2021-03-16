
class FetchStatus:

    def __call__(self, type):

        return dict(
            message='FetchStatus',
            type=type
        )


class Killed:

    def __call__(self, id, service):

        return dict(
            message='Killed',
            id=id,
            service=service
        )


class Id:

    def __call__(self, value, service):

        return dict(
            message='Id',
            value=value,
            service=service
        )


class Identification:

    def __call__(self, name, type, ip, port, service):

        return dict(
            message='Identification',
            name=name,
            type=type,
            ip=ip,
            port=port,
            service=service
        )


class Status:

    def __call__(self, type, payload, id, service):

        return dict(
            message='Status',
            type=type,
            payload=payload,
            id=id,
            service=service
        )


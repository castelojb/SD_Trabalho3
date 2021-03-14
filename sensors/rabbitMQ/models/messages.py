
class FetchStatus:

    def __call__(self, type):

        return dict(
            function='FetchStatus',
            type=type
        )


class Killed:

    def __call__(self, id):

        return dict(
            function='Killed',
            id=id
        )


class Id:

    def __call__(self, value):

        return dict(
            function='Id',
            value=value
        )


class Identification:

    def __call__(self, name, type, ip, port):

        return dict(
            function='Identification',
            name=name,
            type=type,
            ip=ip,
            port=port
        )


class Status:

    def __call__(self, type, payload, id):

        return dict(
            function='Status',
            type=type,
            payload=payload,
            id=id
        )


import abc


class IStorage(abc.ABC):
    @abc.abstractmethod
    def upload_blob():
        raise NotImplementedError

    @abc.abstractmethod
    def download_blob():
        raise NotImplementedError


class IS3(abc.ABC):
    @abc.abstractmethod
    def upload_blob():
        raise NotImplementedError

    @abc.abstractmethod
    def download_blob():
        raise NotImplementedError


class IBigQuery(abc.ABC):
    @abc.abstractmethod
    def create_table():
        raise NotImplementedError

    @abc.abstractmethod
    def append_row():
        raise NotImplementedError


class IModelAdapter(abc.ABC):
    @abc.abstractmethod
    def preprocess():
        pass

    @abc.abstractmethod
    def forward():
        pass

    @abc.abstractmethod
    def postprocess():
        pass


class IOCRService(abc.ABC):
    @abc.abstractmethod
    def preprocess():
        pass

    @abc.abstractmethod
    def forward():
        pass

    @abc.abstractmethod
    def postprocess():
        pass

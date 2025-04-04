from core.utils.domain.interfaces.i_repositories.base_repository import BaseRepository
from core.utils.domain.interfaces.hosts.base_host import BaseHost
from core.utils.application.base_service import Service

from typing import Callable
import inspect

class BaseServiceFactory:
    def __init__(
            self, 
            repositories: dict[str, type[BaseRepository | None]] | dict[str, BaseRepository | None] = dict(), 
            adapters: dict[str, type[BaseHost | None]] | dict[str, BaseHost | None] = dict(), 
            services: dict[str, type[Service | None]] | dict[str, Service | None] = dict(),
        ):
        
        self._services = services
        self._repositories = repositories
        self._adapters = adapters

    def create_service(self, service_class: type[Service], adapter_args: dict = {}, repository_args: dict = {}, service_args: dict = {}) -> Service:
        kwargs = {}

        for cls in inspect.getmro(service_class):
            if cls == object:
                break

            signature = inspect.signature(cls.__init__)
            for name, param in signature.parameters.items():
                if name == 'self':
                    continue

                if name in self._repositories and name not in kwargs:
                    init_args = repository_args.get(name, None)
                    if isinstance(self._repositories[name], Callable):
                        kwargs[name] = self._repositories[name](**init_args) if init_args else self._repositories[name]() 
                    else:
                        kwargs[name] = self._repositories[name]
                elif name in self._adapters and name not in kwargs:
                    init_args = adapter_args.get(name, None)
                    if isinstance(self._adapters[name], Callable):
                        kwargs[name] = self._adapters[name](**init_args) if init_args else self._adapters[name]()
                    else:
                        kwargs[name] = self._adapters[name]
                elif name in self._services and name not in kwargs:
                    init_args = service_args.get(name, None)
                    if isinstance(self._services[name], Callable):
                        kwargs[name] = self._services[name](**init_args) if init_args else self._services[name]()
                    else:
                        kwargs[name] = self._services[name]
                elif param.default is not inspect.Parameter.empty and name not in kwargs:
                    kwargs[name] = param.default

        return service_class(**kwargs)
    

class LazyDependencyInjector:
    """
        This is so-called injector handles service dependencies like repositories, adapters, and other services
        within the context of the RESTful approach. To put it simply, the injector is supposed to pass on dependencies
        instead of initialization, so we would have an opportunity to use lazy-loading within services.
    """
    def __init__(self, repositories: dict[str, type[BaseRepository]] = {}, adapters: dict[str, type[BaseHost]] = {}, services: dict[str, type[Service]] = {}):
        self._services = services
        self._repositories = repositories
        self._adapters = adapters

    def load_service(self, service_class: type[Service]) -> Service:
        kwargs = {}

        for cls in inspect.getmro(service_class):
            if cls == object:
                break

            signature = inspect.signature(cls.__init__)
            for name, param in signature.parameters.items():
                if name == 'self':
                    continue

                if name in self._repositories and name not in kwargs:
                    kwargs[name] = self._repositories[name]
                elif name in self._adapters and name not in kwargs:
                    kwargs[name] = self._adapters[name]
                elif name in self._services and name not in kwargs:
                    kwargs[name] = self._services[name]
                elif param.default is not inspect.Parameter.empty and name not in kwargs:
                    kwargs[name] = param.default

        return service_class(**kwargs)

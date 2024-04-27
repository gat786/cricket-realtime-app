FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /src

COPY frontend-blazor.csproj .

RUN dotnet restore frontend-blazor.csproj

COPY . .

RUN dotnet build -o /app/build

FROM build as publish

RUN dotnet publish -o /app/publish /p:UseAppHost=false


FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
EXPOSE 8080
COPY --from=publish /app/publish .

CMD ["dotnet", "frontend-blazor.dll"]

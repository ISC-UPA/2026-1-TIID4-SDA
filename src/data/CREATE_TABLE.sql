
/*
CREATE TABLE [dbo].[Empleados] (
    [Id]     INT           IDENTITY (1, 1) NOT NULL,
    [Nombre] NVARCHAR (50) NULL,
    CONSTRAINT [PK_Empleados] PRIMARY KEY CLUSTERED ([Id] ASC)
);
*/

use MiAppDB
drop table if exists dbo.Empleados
GO

CREATE TABLE dbo.Empleados (
	EmpleadoID INT PRIMARY KEY,
	Nombre NVARCHAR(100)
);

insert into dbo.Empleados values (1, 'Juan');
insert into dbo.Empleados values (2, 'Maria');
GO


